import React, { useEffect } from 'react';
import { Routes, Route, Navigate, useLocation, useNavigate } from 'react-router-dom';
import { AnimatePresence } from 'framer-motion';
import { useAssessmentStore } from './store/assessmentStore';
import { MajorSelectionPage } from './pages/MajorSelectionPage';
import { QuestionPage } from './pages/QuestionPage';
import { LoadingPage } from './pages/LoadingPage';
import { ResultPage } from './pages/ResultPage';

function App() {
  const { currentStep, initialize } = useAssessmentStore();
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    initialize().catch(err => {
      console.error('初始化失败:', err);
      alert('数据加载失败，请刷新页面重试');
    });
  }, [initialize]);

  // Auto-navigate based on currentStep
  useEffect(() => {
    const path = location.pathname;
    if (currentStep === 'major' && path !== '/') {
      navigate('/', { replace: true });
    } else if (currentStep === 'questions' && path !== '/quiz') {
      navigate('/quiz', { replace: true });
    } else if (currentStep === 'loading' && path !== '/loading') {
      navigate('/loading', { replace: true });
    } else if (currentStep === 'result' && path !== '/result') {
      navigate('/result', { replace: true });
    }
  }, [currentStep, location.pathname, navigate]);

  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={<MajorSelectionPage />} />
        <Route path="/quiz" element={<QuestionPage />} />
        <Route path="/loading" element={<LoadingPage />} />
        <Route path="/result" element={<ResultPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AnimatePresence>
  );
}

export default App;
