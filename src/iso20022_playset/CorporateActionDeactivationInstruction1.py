from . import base_types
import CorporateActionOption2
import ISODateTime

class CorporateActionDeactivationInstruction1(base_types._BaseFieldType):

	__slots__ = ["_DeactvtnDtAndTm", "_OptnDtls"]
	@property
	def DeactvtnDtAndTm(self):
		return self._DeactvtnDtAndTm

	@DeactvtnDtAndTm.setter
	def DeactvtnDtAndTm(self, value):
		self._DeactvtnDtAndTm = value if type(value) != auto else self.make_default("DeactvtnDtAndTm")

	@DeactvtnDtAndTm.deleter
	def DeactvtnDtAndTm(self):
		del self._DeactvtnDtAndTm
		self._DeactvtnDtAndTm = None

	@property
	def OptnDtls(self):
		return self._OptnDtls

	@OptnDtls.setter
	def OptnDtls(self, value):
		self._OptnDtls = value if type(value) != auto else self.make_default("OptnDtls")

	@OptnDtls.deleter
	def OptnDtls(self):
		del self._OptnDtls
		self._OptnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeactvtnDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnDtls', type=CorporateActionOption2, min=0, max=None, mutex_group=None, array=True),
	))

