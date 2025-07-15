package it.smartcommunitylabdhub.runtime.hpcdl.specs;

import it.smartcommunitylabdhub.commons.annotations.common.SpecType;
import it.smartcommunitylabdhub.commons.models.entities.EntityName;
import it.smartcommunitylabdhub.commons.models.function.FunctionTaskBaseSpec;
import it.smartcommunitylabdhub.runtime.hpcdl.HPCDLRuntime;
import java.io.Serializable;
import java.util.Map;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@SpecType(runtime = HPCDLRuntime.RUNTIME, kind = HPCDLJobTaskSpec.KIND, entity = EntityName.TASK)
public class HPCDLJobTaskSpec extends FunctionTaskBaseSpec {

    public static final String KIND = "hpcdl+job";

    public HPCDLJobTaskSpec(Map<String, Serializable> data) {
        configure(data);
    }
}
