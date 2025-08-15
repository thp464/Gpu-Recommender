import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import { DesktopOutlined, InfoCircleOutlined } from '@ant-design/icons';
import GPURecommender from './components/GPURecommender';
import AboutGPU from './components/AboutGPU';
import './App.css';

const { Header, Content } = Layout;

const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<string>('recommender');

  const menuItems = [
    {
      key: 'recommender',
      icon: <DesktopOutlined />,
      label: 'GPU Recommender',
    },
    {
      key: 'about',
      icon: <InfoCircleOutlined />,
      label: 'All About GPUs',
    },
  ];

  const renderContent = () => {
    switch (currentPage) {
      case 'about':
        return <AboutGPU />;
      case 'recommender':
      default:
        return <GPURecommender />; 
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ color: 'white', fontSize: '20px', fontWeight: 'bold', marginRight: '24px' }}>
          🎮 GPU Recommender
        </div>
        <Menu
          theme="dark"
          mode="horizontal"
          selectedKeys={[currentPage]}
          items={menuItems}
          onClick={({ key }) => setCurrentPage(key)}
          style={{ flex: 1, minWidth: 0 }}
        />
      </Header>
      <Content style={{ padding: '0', backgroundColor: '#f0f2f5' }}>
        {renderContent()}
      </Content>
    </Layout>
  );
};

export default App;