import { configure } from '@storybook/react';

function loadStories() {
  require('../src/stories/InputStory');
  require('../src/stories/NewCounterStory');
}

configure(loadStories, module);