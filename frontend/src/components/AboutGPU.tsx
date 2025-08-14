import React from 'react';
import { Typography, Card, Row, Col, Space } from 'antd';
import { DesktopOutlined } from '@ant-design/icons';

const { Title, Text, Paragraph } = Typography;

const AboutGPU: React.FC = () => {
  return (
    <div style={{ padding: '24px', maxWidth: '1200px', margin: '0 auto' }}>
      <Title level={1}>
        <DesktopOutlined /> All About GPUs
      </Title>
      <Text type="secondary" style={{ fontSize: '16px' }}>
        Everything you need to know about Graphics Processing Units
      </Text>

      {/* GPU Basics */}
      <Card style={{ marginTop: '24px' }}>
        <Title level={2}>What is a GPU?</Title>
        <Paragraph>
          A <Text strong>Graphics Processing Unit (GPU)</Text> is a specialized processor 
          designed to handle graphics rendering and parallel computations.
        </Paragraph>
      </Card>

      <Row gutter={24} style={{ marginTop: '24px' }}>
        <Col span={12}>
          <Card>
            <Title level={3}>VRAM</Title>
            <Paragraph>
              Video Random Access Memory stores textures and graphics data.
            </Paragraph>
          </Card>
        </Col>
        
        <Col span={12}>
          <Card>
            <Title level={3}>FPS</Title>
            <Paragraph>
              Frames Per Second measures rendering performance.
            </Paragraph>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default AboutGPU;