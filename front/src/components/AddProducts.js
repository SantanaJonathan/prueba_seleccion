import react, { useState } from "react";
import { Form, Button, Card } from "react-bootstrap";

const AddProducts = () => {
  const [productInfo, setProductInfo] = useState({
    ProductName: "",
    ProductCode: "",
    QuantityInStock: "",
    QuantitySold: "",
    UnitPrice: "",
    Revenue: "",
  });

  const updateForm = (e) => {
    setProductInfo({ ...productInfo, [e.target.name]: e.target.value });
  };

  const postData = async (e) => {
    e.preventDefault();
    console.log(productInfo);

    const url = "http://localhost:8000/product";

    const response = await fetch(url, {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify({
        name: productInfo["ProductName"],
        code: productInfo["ProductCode"],
        quantity_in_stock: productInfo["QuantityInStock"],
        quantity_sold: productInfo["QuantitySold"],
        unit_price: productInfo["UnitPrice"],
        revenue: productInfo["Revenue"],
      }),
    });
    response.json().then((response) => {
      if (response.status === "ok") {
        alert("Product added successfully");
      } else {
        alert("Failed to add product");
      }
    });
    setProductInfo({
      ProductName: "",
      ProductCode: "",
      QuantityInStock: "",
      QuantitySold: "",
      UnitPrice: "",
      Revenue: "",
    });
  };

  return (
    <Card>
      <Card.Body>
        <Form onSubmit={postData}>
          <Form.Group controlId="ProductName">
            <Form.Label>Product Name</Form.Label>
            <Form.Control
              type="text"
              name="ProductName"
              value={productInfo.ProductName}
              onChange={updateForm}
              placeholder="Product Name"
            />
          </Form.Group>

          <Form.Group controlId="ProductCode">
            <Form.Label>ProductCode</Form.Label>
            <Form.Control
              type="text"
              name="ProductCode"
              value={productInfo.ProductCode}
              onChange={updateForm}
              placeholder="Product Code"
            />
          </Form.Group>

          <Form.Group controlId="QuantityInStock">
            <Form.Label>Quantity In Stock</Form.Label>
            <Form.Control
              type="number"
              name="QuantityInStock"
              value={productInfo.QuantityInStock}
              onChange={updateForm}
              placeholder="Quantity In Stock"
            />
          </Form.Group>

          <Form.Group controlId="QuantitySold">
            <Form.Label>Quantity Sold</Form.Label>
            <Form.Control
              type="number"
              name="QuantitySold"
              value={productInfo.QuantitySold}
              onChange={updateForm}
              placeholder="Quantity Sold"
            />
          </Form.Group>

          <Form.Group controlId="UnitPrice">
            <Form.Label>Unit Price</Form.Label>
            <Form.Control
              type="number"
              name="UnitPrice"
              value={productInfo.UnitPrice}
              onChange={updateForm}
              placeholder="Unit Price"
            />
          </Form.Group>

          <Form.Group controlId="Revenue">
            <Form.Label>Revenue</Form.Label>
            <Form.Control
              type="number"
              name="Revenue"
              value={productInfo.Revenue}
              onChange={updateForm}
              placeholder="Revenue"
            />
          </Form.Group>

          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
};

export default AddProducts;
