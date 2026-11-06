# Rà soát bảo mật và học tập

Tiếng Việt · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Học OWASP, viết mã an toàn hơn và rà soát commit của bất kỳ dự án nào. Skill này cũng bao gồm MCP, ứng dụng LLM, tác tử AI và gói skill.

## Cài đặt

Sao chép thư mục security-review vào .agents/skills/ của dự án. Gọi skill từ dự án bạn muốn làm việc.

## Ví dụ

```text
$security-review Rà soát commit này và tiếp tục hoạt động cho các commit tiếp theo.
$security-review Giúp tôi triển khai tính năng này cùng kiểm thử chức năng và bảo mật.
$security-review Dạy tôi bảo mật MCP bằng bài trắc nghiệm, mỗi lần một câu hỏi.
```

## Hoạt động và giới hạn

Skill kiểm tra nguồn chính thức hiện hành, giải thích phát hiện và cách sửa, đồng thời báo rõ những kiểm thử đã thực sự chạy. Trong quá trình lập trình, skill giúp kiểm tra việc sử dụng hợp lệ và hành động trái phép. Bài học được điều chỉnh theo câu trả lời.

Skill chỉ hoạt động trong phiên của tác tử; không theo dõi Git sau khi phiên kết thúc. Bản dịch này do AI tạo và chưa được người bản ngữ rà soát.

## Tài liệu tham khảo

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
