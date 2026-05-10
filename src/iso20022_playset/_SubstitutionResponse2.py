from . import base_types
from .CollateralSubstitutionResponse1 import CollateralSubstitutionResponse1
from .CollateralSubstitutionResponse3 import CollateralSubstitutionResponse3
from .Status4Code import Status4Code

class SubstitutionResponse2(base_types._BaseFieldType):

	__slots__ = ["_CollSbstitnRjctnDtls", "_CollSbstitnAccptncDtls", "_RspnTp"]
	@property
	def CollSbstitnRjctnDtls(self):
		return self._CollSbstitnRjctnDtls

	@CollSbstitnRjctnDtls.setter
	def CollSbstitnRjctnDtls(self, value):
		self._CollSbstitnRjctnDtls = value if type(value) != base_types.auto else self.make_default("CollSbstitnRjctnDtls")

	@CollSbstitnRjctnDtls.deleter
	def CollSbstitnRjctnDtls(self):
		del self._CollSbstitnRjctnDtls
		self._CollSbstitnRjctnDtls = None

	@property
	def CollSbstitnAccptncDtls(self):
		return self._CollSbstitnAccptncDtls

	@CollSbstitnAccptncDtls.setter
	def CollSbstitnAccptncDtls(self, value):
		self._CollSbstitnAccptncDtls = value if type(value) != base_types.auto else self.make_default("CollSbstitnAccptncDtls")

	@CollSbstitnAccptncDtls.deleter
	def CollSbstitnAccptncDtls(self):
		del self._CollSbstitnAccptncDtls
		self._CollSbstitnAccptncDtls = None

	@property
	def RspnTp(self):
		return self._RspnTp

	@RspnTp.setter
	def RspnTp(self, value):
		self._RspnTp = value if type(value) != base_types.auto else self.make_default("RspnTp")

	@RspnTp.deleter
	def RspnTp(self):
		del self._RspnTp
		self._RspnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSbstitnRjctnDtls', type=CollateralSubstitutionResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnAccptncDtls', type=CollateralSubstitutionResponse1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTp', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
	))

