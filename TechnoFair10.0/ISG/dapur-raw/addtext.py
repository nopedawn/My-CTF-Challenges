import cv2

def write_text_on_video(text, video_file):
    cap = cv2.VideoCapture(video_file)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    start_time = 10  # Detik mulai penambahan teks
    start_frame = int(start_time * fps)
    frame_count = 0
    char_index = 0
    total_chars = len(text)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_file = "output_video.mp4"
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count >= start_frame and char_index < total_chars:
            char = text[char_index]
            scale = 2  # Nilai skala untuk memperbesar teks
            thickness = 2  # Ketebalan teks
            text_size, _ = cv2.getTextSize(char, cv2.FONT_HERSHEY_SIMPLEX, scale, thickness)
            text_x = int((frame_width - text_size[0]) / 2)
            text_y = int((frame_height + text_size[1]) / 2)
            cv2.putText(frame, char, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 255, 0), thickness)
            char_index += 1

        out.write(frame)
        frame_count += 1

    cap.release()
    out.release()

    print(f"Video with text written successfully to {output_file}.")

text = "TechnoFairCTF{d0_n0t_5t0r3_y0ur_1mp0rt4nt_d4t4_1nt0_y0utu63_1nf1n1t3_5T0r493_9L1tch}"
video_file = "video.mp4"

write_text_on_video(text, video_file)
