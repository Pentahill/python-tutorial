import cv2

def convertCodec(src, outFile, fourcc):
    vc = cv2.VideoCapture(src)

    fps = vc.get(cv2.CAP_PROP_FPS)
    size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    vw = cv2.VideoWriter(outFile, cv2.VideoWriter_fourcc(*fourcc), fps, size)

    success, frame = vc.read()
    while success:
        vw.write(frame)
        success, frame = vc.read()

# AVc1 
# need openh264
# convertCodec('./demo.mp4', 'demo_ot_avc1.mp4', 'avc1')

# MPEG-4
# convertCodec('./demo.mp4', 'demo_ot_mp4v.mp4', 'mp4v')

# MPEG-4
# convertCodec('./demo.mp4', 'demo_ot_XVID.avi', 'XVID')
# convertCodec('./demo.mp4', 'demo_ot_XVID.mp4', 'XVID')

# convertCodec('./demo.mp4', 'demo_ot_i420.avi', 'I420')

# OpenCV: FFMPEG: tag 0x30387076/'vp80' is not supported with codec id 139 and format 'webm / WebM'
# convertCodec('./demo.mp4', 'demo_ot_vp80.webm', 'vp80')

# need openh264
convertCodec('./demo.mp4', 'demo_ot_h264.mp4', 'H264')


