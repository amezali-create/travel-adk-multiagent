from travel_assistant.agent import root_agent


def test_root_agent_name():
    assert root_agent.name == "travel_coordinator_agent"


def test_root_agent_has_sub_agents():
    # 4 agentes de la guía + LocalCultureAgent del reto
    assert len(root_agent.sub_agents) == 5


def test_sub_agent_names():
    names = {agent.name for agent in root_agent.sub_agents}

    assert "web_search_agent" in names
    assert "itinerary_agent" in names
    assert "budget_agent" in names
    assert "risk_reviewer_agent" in names
    assert "local_culture_agent" in names


def test_local_culture_agent_has_its_tool():
    culture_agent = next(a for a in root_agent.sub_agents if a.name == "local_culture_agent")

    assert [tool.__name__ for tool in culture_agent.tools] == ["get_local_culture_info"]
