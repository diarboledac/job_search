import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { App } from "./App";

describe("App", () => {
  it("renders the platform shell", () => {
    render(<App />);

    expect(
      screen.getByRole("heading", { name: "CareerPilot-AI" })
    ).toBeInTheDocument();
    expect(screen.getByText("AI Career Platform")).toBeInTheDocument();
  });
});
