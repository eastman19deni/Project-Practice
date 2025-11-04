#!/usr/bin/env python3
import argparse
from src.real_time_detector import RealTimeDetector
from src.video_processor import VideoProcessor
from src.utils.config import load_config

def main():
    parser = argparse.ArgumentParser(description="Classroom People Counter")
    parser.add_argument('--mode', choices=['realtime','video'], default='realtime')
    parser.add_argument('--source', default=0, help='camera index or video file path')
    parser.add_argument('--config', default='config/app_config.yaml')
    args = parser.parse_args()

    cfg = load_config(args.config)

    if args.mode == 'realtime':
        detector = RealTimeDetector(cfg)
        detector.run(source=args.source)
    else:
        processor = VideoProcessor(cfg)
        processor.process_video(args.source)

if __name__ == '__main__':
    main()
