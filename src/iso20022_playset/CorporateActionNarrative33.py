import base_types
import RestrictedFINXMax350Text

class CorporateActionNarrative33(base_types._BaseFieldType):

	__slots__ = ["_InfToCmplyWth", "_FXInstrsAddtlInf", "_InstrAddtlInf", "_DlvryDtls"]
	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if type(value) != auto else self.make_default("InfToCmplyWth")

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = None

	@property
	def FXInstrsAddtlInf(self):
		return self._FXInstrsAddtlInf

	@FXInstrsAddtlInf.setter
	def FXInstrsAddtlInf(self, value):
		self._FXInstrsAddtlInf = value if type(value) != auto else self.make_default("FXInstrsAddtlInf")

	@FXInstrsAddtlInf.deleter
	def FXInstrsAddtlInf(self):
		del self._FXInstrsAddtlInf
		self._FXInstrsAddtlInf = None

	@property
	def InstrAddtlInf(self):
		return self._InstrAddtlInf

	@InstrAddtlInf.setter
	def InstrAddtlInf(self, value):
		self._InstrAddtlInf = value if type(value) != auto else self.make_default("InstrAddtlInf")

	@InstrAddtlInf.deleter
	def InstrAddtlInf(self):
		del self._InstrAddtlInf
		self._InstrAddtlInf = None

	@property
	def DlvryDtls(self):
		return self._DlvryDtls

	@DlvryDtls.setter
	def DlvryDtls(self, value):
		self._DlvryDtls = value if type(value) != auto else self.make_default("DlvryDtls")

	@DlvryDtls.deleter
	def DlvryDtls(self):
		del self._DlvryDtls
		self._DlvryDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfToCmplyWth', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FXInstrsAddtlInf', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrAddtlInf', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryDtls', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
	))

