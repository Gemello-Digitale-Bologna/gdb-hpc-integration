package it.smartcommunitylabdhub.runtime.hpcdl.specs;

import io.swagger.v3.oas.annotations.media.Schema;
import it.smartcommunitylabdhub.commons.annotations.common.SpecType;
import it.smartcommunitylabdhub.commons.models.entities.EntityName;
import it.smartcommunitylabdhub.commons.models.function.FunctionBaseSpec;
import it.smartcommunitylabdhub.runtime.hpcdl.HPCDLRuntime;
import java.io.Serializable;
import java.util.Map;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@SpecType(runtime = HPCDLRuntime.RUNTIME, kind = HPCDLRuntime.RUNTIME, entity = EntityName.FUNCTION)
public class HPCDLFunctionSpec extends FunctionBaseSpec {

    @Schema(title = "fields.hpcdl.image.title", description = "fields.hpcdl.image.description")
    private String image;

    @Schema(title = "fields.hpcdl.command.title", description = "fields.hpcdl.command.description")
    private String command;

    public HPCDLFunctionSpec(Map<String, Serializable> data) {
        configure(data);
    }

    @Override
    public void configure(Map<String, Serializable> data) {
        super.configure(data);

        HPCDLFunctionSpec spec = mapper.convertValue(data, HPCDLFunctionSpec.class);

        this.command = spec.getCommand();
        this.image = spec.getImage();
    }

}
