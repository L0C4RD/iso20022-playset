from . import base_types
import SecuritiesBalanceType1Code
import Extended350Code
import AdditionalBalanceInformation2
import SubBalanceQuantity1Choice

class SubBalanceInformation2(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_XtndedSubBalTp", "_AddtlBalBrkdwnDtls", "_SubBalTp"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def XtndedSubBalTp(self):
		return self._XtndedSubBalTp

	@XtndedSubBalTp.setter
	def XtndedSubBalTp(self, value):
		self._XtndedSubBalTp = value if type(value) != auto else self.make_default("XtndedSubBalTp")

	@XtndedSubBalTp.deleter
	def XtndedSubBalTp(self):
		del self._XtndedSubBalTp
		self._XtndedSubBalTp = None

	@property
	def AddtlBalBrkdwnDtls(self):
		return self._AddtlBalBrkdwnDtls

	@AddtlBalBrkdwnDtls.setter
	def AddtlBalBrkdwnDtls(self, value):
		self._AddtlBalBrkdwnDtls = value if type(value) != auto else self.make_default("AddtlBalBrkdwnDtls")

	@AddtlBalBrkdwnDtls.deleter
	def AddtlBalBrkdwnDtls(self):
		del self._AddtlBalBrkdwnDtls
		self._AddtlBalBrkdwnDtls = None

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if type(value) != auto else self.make_default("SubBalTp")

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedSubBalTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwnDtls', type=AdditionalBalanceInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubBalTp', type=SecuritiesBalanceType1Code, min=0, max=1, mutex_group=1, array=False),
	))

