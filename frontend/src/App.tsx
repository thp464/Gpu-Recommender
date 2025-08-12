import React, { useState, useEffect } from 'react';
import {
  Card,
  Select,
  Slider,
  Button,
  Table,
  Typography,
  Space,
  Alert,
  Spin,
  Row,
  Col
} from 'antd';
import axios from 'axios';
import './App.css';

const { Title, Text } = Typography;
const { Option } = Select;

interface GPURecommendation {
  gpu: string;
  fps: number;
  vram_mb: number;
  price: number;
}

interface PriceRange {
  min_price: number;
  max_price: number;
}

const API_BASE_URL = 'http://localhost:8000';

const App: React.FC = () => {
  const [resolution, setResolution] = useState<string>('1080p');
  const [minFps, setMinFps] = useState<number>(60);
  const [maxBudget, setMaxBudget] = useState<number>(1000);
  const [recommendations, setRecommendations] = useState<GPURecommendation[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [priceRange, setPriceRange] = useState<PriceRange>({ min_price: 0, max_price: 2000 });

  useEffect(() => {
    fetchPriceRange();
  }, []);

  const fetchPriceRange = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/price-range`);
      setPriceRange(response.data);
      setMaxBudget(response.data.max_price);
    } catch (err) {
      console.error('Error fetching price range:', err);
    }
  };

  const getRecommendations = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.post(`${API_BASE_URL}/api/recommendations`, {
        resolution,
        min_fps: minFps,
        max_budget: maxBudget === priceRange.max_price ? null : maxBudget
      });
      
      setRecommendations(response.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to fetch recommendations');
    } finally {
      setLoading(false);
    }
  };

  const columns = [
    {
      title: 'GPU',
      dataIndex: 'gpu',
      key: 'gpu',
      width: '40%',
    },
    {
      title: 'FPS',
      dataIndex: 'fps',
      key: 'fps',
      width: '15%',
      render: (fps: number) => Math.round(fps),
    },
    {
      title: 'VRAM',
      dataIndex: 'vram_mb',
      key: 'vram_mb',
      width: '20%',
      render: (vram: number) => `${(vram / 1024).toFixed(1)} GB`,
    },
    {
      title: 'Price',
      dataIndex: 'price',
      key: 'price',
      width: '25%',
      render: (price: number) => `$${price.toFixed(0)}`,
    },
  ];

  return (
    <div style={{ padding: '24px', maxWidth: '1200px', margin: '0 auto' }}>
      <Title level={1}>🎮 GPU Recommender</Title>
      <Text type="secondary">Find the perfect GPU for your gaming needs</Text>
      
      <Row gutter={24} style={{ marginTop: '24px' }}>
        <Col span={8}>
          <Card title="GPU Preferences" size="small">
            <Space direction="vertical" size="large" style={{ width: '100%' }}>
              <div>
                <Text strong>Target Resolution</Text>
                <Select
                  value={resolution}
                  onChange={setResolution}
                  style={{ width: '100%', marginTop: '8px' }}
                  size="large"
                >
                  <Option value="1080p">1080p (Full HD)</Option>
                  <Option value="1440p">1440p (2K)</Option>
                  <Option value="4k">4K (Ultra HD)</Option>
                </Select>
              </div>

              <div>
                <Text strong>Minimum FPS: {minFps}</Text>
                <Slider
                  value={minFps}
                  onChange={setMinFps}
                  min={30}
                  max={240}
                  step={10}
                  style={{ marginTop: '16px' }}
                  marks={{
                    30: '30',
                    60: '60',
                    120: '120',
                    240: '240'
                  }}
                />
              </div>

              <div>
                <Text strong>Maximum Budget: ${maxBudget}</Text>
                <Slider
                  value={maxBudget}
                  onChange={setMaxBudget}
                  min={priceRange.min_price}
                  max={priceRange.max_price}
                  step={50}
                  style={{ marginTop: '16px' }}
                  marks={{
                    [priceRange.min_price]: `$${priceRange.min_price}`,
                    [Math.round(priceRange.max_price / 2)]: `$${Math.round(priceRange.max_price / 2)}`,
                    [priceRange.max_price]: `$${priceRange.max_price}`
                  }}
                />
              </div>

              <Button
                type="primary"
                size="large"
                onClick={getRecommendations}
                loading={loading}
                style={{ width: '100%' }}
              >
                Get Recommendations
              </Button>
            </Space>
          </Card>
        </Col>

        <Col span={16}>
          {error && (
            <Alert
              message="Error"
              description={error}
              type="error"
              closable
              style={{ marginBottom: '24px' }}
            />
          )}

          {loading ? (
            <Card>
              <div style={{ textAlign: 'center', padding: '48px' }}>
                <Spin size="large" />
                <div style={{ marginTop: '16px' }}>
                  <Text>Finding the best GPUs for you...</Text>
                </div>
              </div>
            </Card>
          ) : recommendations.length > 0 ? (
            <Card title={`Recommended GPUs for ${resolution} gaming at ${minFps}+ FPS`}>
              <Table
                dataSource={recommendations}
                columns={columns}
                pagination={false}
                rowKey="gpu"
                size="middle"
              />
            </Card>
          ) : (
            <Card>
              <div style={{ textAlign: 'center', padding: '48px' }}>
                <Text type="secondary">
                  Select your preferences and click "Get Recommendations" to find the perfect GPU!
                </Text>
              </div>
            </Card>
          )}
        </Col>
      </Row>
    </div>
  );
};

export default App;