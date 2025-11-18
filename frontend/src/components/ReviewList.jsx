import React, { useEffect, useState } from "react";

export default function ReviewList() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/reviews")
      .then((res) => res.json())
      .then(setReviews);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>📦 Product Reviews</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>User</th>
            <th>Product</th>
            <th>Review</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {reviews.map((r) => (
            <tr key={r.id}>
              <td>{r.user_name}</td>
              <td>{r.product_name}</td>
              <td>{r.product_review}</td>
              <td>{new Date(r.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
