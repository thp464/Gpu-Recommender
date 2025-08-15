import React from 'react';
import {
  Typography,
  Card,
  Row,
  Col,
  Space,
  Divider,
  Alert,
  Tag,
  List,
  Collapse
} from 'antd';
import {
  DesktopOutlined,
  ThunderboltOutlined,
  DatabaseOutlined,
  TrophyOutlined,
  DollarOutlined,
  ExperimentOutlined,
  ShoppingCartOutlined,
  BulbOutlined
} from '@ant-design/icons';

const { Title, Text, Paragraph } = Typography;
const { Panel } = Collapse;

const AboutGPU: React.FC = () => {
  const vramRequirements = [
    { resolution: '1080p Gaming', vram: '6-8 GB VRAM' },
    { resolution: '1440p Gaming', vram: '8-12 GB VRAM' },
    { resolution: '4K Gaming', vram: '12+ GB VRAM' },
    { resolution: 'Content Creation', vram: '16+ GB VRAM recommended' }
  ];

  const fpsTargets = [
    { target: '30 FPS', description: 'Minimum for playable gaming' },
    { target: '60 FPS', description: 'Smooth gaming experience' },
    { target: '120+ FPS', description: 'Competitive gaming, high refresh rate monitors' },
    { target: '240+ FPS', description: 'Professional esports' }
  ];

  const budgetTiers = [
    { tier: 'Entry', budget: '$200-400', examples: 'GTX 1660 Super, RX 6500 XT' },
    { tier: 'Mid-range', budget: '$400-700', examples: 'RTX 4060, RX 7600' },
    { tier: 'High-end', budget: '$700-1200+', examples: 'RTX 4080, RX 7900 XTX' },
    { tier: 'Enthusiast', budget: '$1200+', examples: 'RTX 4090' }
  ];

  return (
    <div style={{ padding: '24px', maxWidth: '1200px', margin: '0 auto' }}>
      <Title level={1}>
        <DesktopOutlined /> All About GPUs
      </Title>
      <Text type="secondary" style={{ fontSize: '16px' }}>
        Everything you need to know about Graphics Processing Units
      </Text>

      <Divider />

      {/* GPU Basics */}
      <Card style={{ marginBottom: '24px' }}>
        <Title level={2}>
          <DesktopOutlined /> What is a GPU?
        </Title>
        <Paragraph style={{ fontSize: '16px' }}>
          A <Text strong>Graphics Processing Unit (GPU)</Text> is a specialized processor designed to handle 
          graphics rendering and parallel computations. Originally created for rendering images and video, 
          modern GPUs are essential for:
        </Paragraph>
        <Row gutter={[16, 16]}>
          <Col span={12}>
            <List
              size="small"
              dataSource={[
                'Gaming and entertainment',
                'Video editing and content creation',
                'AI and machine learning'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Col>
          <Col span={12}>
            <List
              size="small"
              dataSource={[
                'Cryptocurrency mining',
                'Scientific computing',
                '3D rendering and animation'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Col>
        </Row>
      </Card>

      <Row gutter={24}>
        {/* VRAM Section */}
        <Col span={12}>
          <Card style={{ marginBottom: '24px', height: '100%' }}>
            <Title level={2}>
              <DatabaseOutlined /> What is VRAM?
            </Title>
            <Paragraph>
              <Text strong>Video Random Access Memory (VRAM)</Text> is dedicated memory on your graphics card that stores:
            </Paragraph>
            <List
              size="small"
              dataSource={[
                'Textures and image data',
                'Frame buffers',
                'Shader programs',
                '3D models and geometry'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
            
            <Title level={4} style={{ marginTop: '16px' }}>VRAM Requirements by Resolution:</Title>
            <Space direction="vertical" style={{ width: '100%' }}>
              {vramRequirements.map((req, index) => (
                <div key={index} style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <Text strong>{req.resolution}:</Text>
                  <Tag color="blue">{req.vram}</Tag>
                </div>
              ))}
            </Space>
          </Card>
        </Col>

        {/* FPS Section */}
        <Col span={12}>
          <Card style={{ marginBottom: '24px', height: '100%' }}>
            <Title level={2}>
              <ThunderboltOutlined /> What is FPS?
            </Title>
            <Paragraph>
              <Text strong>Frames Per Second (FPS)</Text> measures how many images your GPU can render each second.
            </Paragraph>
            
            <Title level={4}>Common FPS Targets:</Title>
            <Space direction="vertical" style={{ width: '100%' }}>
              {fpsTargets.map((fps, index) => (
                <div key={index}>
                  <Text strong style={{ color: '#1890ff' }}>{fps.target}:</Text>
                  <Text style={{ marginLeft: '8px' }}>{fps.description}</Text>
                </div>
              ))}
            </Space>

            <Title level={4} style={{ marginTop: '16px' }}>Factors Affecting FPS:</Title>
            <List
              size="small"
              dataSource={[
                'GPU performance',
                'Game settings (resolution, graphics quality)',
                'CPU performance',
                'Available VRAM'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Card>
        </Col>
      </Row>

      {/* GPU Types */}
      <Card style={{ marginBottom: '24px' }}>
        <Title level={2}>
          <TrophyOutlined /> Types of GPUs
        </Title>
        <Row gutter={24}>
          <Col span={12}>
            <Title level={4}>Gaming GPUs</Title>
            <Collapse ghost>
              <Panel header="NVIDIA GeForce Series" key="nvidia">
                <List
                  size="small"
                  dataSource={[
                    'RTX 40 Series (RTX 4090, 4080, 4070)',
                    'RTX 30 Series (RTX 3080, 3070, 3060)',
                    'GTX 16 Series (GTX 1660 Super, 1650)'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              </Panel>
              <Panel header="AMD Radeon Series" key="amd">
                <List
                  size="small"
                  dataSource={[
                    'RX 7000 Series (RX 7900 XTX, 7800 XT)',
                    'RX 6000 Series (RX 6800 XT, 6700 XT)',
                    'RX 5000 Series (RX 5700 XT, 5600 XT)'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              </Panel>
            </Collapse>
          </Col>
          
          <Col span={12}>
            <Title level={4}>Professional GPUs</Title>
            <Collapse ghost>
              <Panel header="NVIDIA Quadro/RTX A Series" key="quadro">
                <Paragraph>For CAD, 3D modeling, rendering</Paragraph>
              </Panel>
              <Panel header="AMD Radeon Pro" key="radeon-pro">
                <Paragraph>Professional workstation graphics</Paragraph>
              </Panel>
            </Collapse>
            
            <Title level={5} style={{ marginTop: '16px' }}>Professional Features:</Title>
            <List
              size="small"
              dataSource={['ECC memory', 'Certified drivers', 'Optimized for professional software']}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Col>
        </Row>
      </Card>

      {/* Performance Metrics */}
      <Card style={{ marginBottom: '24px' }}>
        <Title level={2}>
          <ExperimentOutlined /> Key Performance Metrics
        </Title>
        <Title level={4}>When Choosing a GPU, Consider:</Title>
        
        <Row gutter={24}>
          <Col span={12}>
            <Space direction="vertical" size="middle" style={{ width: '100%' }}>
              <div>
                <Text strong>1. Target Resolution</Text>
                <br />
                <Text type="secondary">Higher resolution = more GPU power needed</Text>
              </div>
              
              <div>
                <Text strong>2. Game Types</Text>
                <br />
                <Text type="secondary">AAA games require more power than indie games</Text>
                <br />
                <Text type="secondary">Ray tracing games need RTX/RDNA2+ GPUs</Text>
              </div>
            </Space>
          </Col>
          
          <Col span={12}>
            <Space direction="vertical" size="middle" style={{ width: '100%' }}>
              <div>
                <Text strong>3. Monitor Refresh Rate</Text>
                <br />
                <Text type="secondary">60Hz monitor: 60+ FPS target</Text>
                <br />
                <Text type="secondary">144Hz monitor: 144+ FPS target</Text>
              </div>
              
              <div>
                <Text strong>4. Budget vs Performance</Text>
                <br />
                <Space direction="vertical" size="small">
                  {budgetTiers.map((tier, index) => (
                    <div key={index}>
                      <Tag color="green">{tier.tier}</Tag>
                      <Text>{tier.budget} - {tier.examples}</Text>
                    </div>
                  ))}
                </Space>
              </div>
            </Space>
          </Col>
        </Row>
      </Card>

      {/* Modern Technologies */}
      <Card style={{ marginBottom: '24px' }}>
        <Title level={2}>
          <ExperimentOutlined /> Modern GPU Technologies
        </Title>
        <Row gutter={24}>
          <Col span={12}>
            <Space direction="vertical" size="large" style={{ width: '100%' }}>
              <div>
                <Title level={4}>Ray Tracing</Title>
                <Paragraph>
                  Realistic lighting and reflections:
                </Paragraph>
                <List
                  size="small"
                  dataSource={[
                    'NVIDIA RTX series',
                    'AMD RDNA2+ (RX 6000/7000)',
                    'Significant performance impact'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              </div>
              
              <div>
                <Title level={4}>DLSS/FSR</Title>
                <Paragraph>
                  AI upscaling for better performance:
                </Paragraph>
                <List
                  size="small"
                  dataSource={[
                    'DLSS: NVIDIA RTX cards only',
                    'FSR: Works on most modern GPUs',
                    'Improves FPS with minimal quality loss'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              </div>
            </Space>
          </Col>
          
          <Col span={12}>
            <Space direction="vertical" size="large" style={{ width: '100%' }}>
              <div>
                <Title level={4}>VRAM Buffer</Title>
                <Paragraph>How much VRAM you need:</Paragraph>
                <List
                  size="small"
                  dataSource={[
                    '4GB: 1080p low-medium settings',
                    '8GB: 1080p high, 1440p medium',
                    '12GB+: 1440p/4K high settings'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              </div>
              
              <div>
                <Title level={4}>Power Consumption</Title>
                <Paragraph>GPU power requirements:</Paragraph>
                <List
                  size="small"
                  dataSource={[
                    'Entry: 75-150W',
                    'Mid-range: 150-250W',
                    'High-end: 250-350W',
                    'Enthusiast: 350-450W'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              </div>
            </Space>
          </Col>
        </Row>
      </Card>

      {/* Buying Guide */}
      <Card style={{ marginBottom: '24px' }}>
        <Title level={2}>
          <ShoppingCartOutlined /> GPU Buying Guide
        </Title>
        <Title level={4}>Step-by-Step Guide:</Title>
        
        <Collapse>
          <Panel header="1. 💰 Determine Your Budget" key="budget">
            <List
              dataSource={budgetTiers}
              renderItem={tier => (
                <List.Item>
                  <Text strong>{tier.tier}:</Text> {tier.budget} - {tier.examples}
                </List.Item>
              )}
            />
          </Panel>
          
          <Panel header="2. 🎯 Choose Your Target Resolution" key="resolution">
            <List
              dataSource={[
                '1080p: RTX 4060, RX 7600',
                '1440p: RTX 4070, RX 7700 XT', 
                '4K: RTX 4080+, RX 7900 XTX'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Panel>
          
          <Panel header="3. ⚡ Check Your PSU" key="psu">
            <List
              dataSource={[
                'Ensure adequate wattage',
                'Required power connectors',
                'Quality 80+ rated PSU recommended'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Panel>
          
          <Panel header="4. 🖥️ Consider Your CPU" key="cpu">
            <List
              dataSource={[
                'Avoid CPU bottlenecks',
                'Match GPU tier with CPU tier',
                'Check compatibility with motherboard'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Panel>
          
          <Panel header="5. 🔮 Future-Proofing" key="future">
            <List
              dataSource={[
                'VRAM amount for future games',
                'Ray tracing support',
                'DLSS/FSR compatibility'
              ]}
              renderItem={item => <List.Item>• {item}</List.Item>}
            />
          </Panel>
        </Collapse>
      </Card>

      {/* Pro Tips */}
      <Card>
        <Title level={2}>
          <BulbOutlined /> Pro Tips
        </Title>
        
        <Row gutter={24}>
          <Col span={8}>
            <Alert
              message="Money-Saving Tips"
              description={
                <List
                  size="small"
                  dataSource={[
                    'Buy previous generation GPUs when new ones release',
                    'Consider used GPUs from reputable sellers',
                    'Look for bundle deals with games'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              }
              type="success"
              showIcon
            />
          </Col>
          
          <Col span={8}>
            <Alert
              message="Performance Tips"
              description={
                <List
                  size="small"
                  dataSource={[
                    'Update GPU drivers regularly',
                    'Monitor GPU temperatures (keep under 80°C)',
                    'Ensure adequate case ventilation',
                    'Use MSI Afterburner for monitoring'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              }
              type="info"
              showIcon
            />
          </Col>
          
          <Col span={8}>
            <Alert
              message="Future Considerations"
              description={
                <List
                  size="small"
                  dataSource={[
                    'Games are requiring more VRAM over time',
                    'Ray tracing is becoming standard',
                    '1440p is becoming the new 1080p'
                  ]}
                  renderItem={item => <List.Item>• {item}</List.Item>}
                />
              }
              type="warning"
              showIcon
            />
          </Col>
        </Row>
        
        <Alert
          message="💡 Ready to find your perfect GPU?"
          description="Use our GPU Recommender tool to get personalized suggestions based on your needs and budget!"
          type="success"
          showIcon
          style={{ marginTop: '24px' }}
          action={
            <Text strong style={{ color: '#52c41a' }}>
              Get Started →
            </Text>
          }
        />
      </Card>
    </div>
  );
};

export default AboutGPU;