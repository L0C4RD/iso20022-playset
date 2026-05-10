import base_types
import AdditionalBalanceInformation20
import QuantityBreakdown57
import SubBalanceType11Choice
import Balance21
import Max140Text

class SubBalanceInformation20(base_types._BaseFieldType):

	__slots__ = ["_QtyBrkdwn", "_AddtlBalBrkdwnDtls", "_SubBalTp", "_SubBalAddtlDtls", "_Qty"]
	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

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

	@property
	def SubBalAddtlDtls(self):
		return self._SubBalAddtlDtls

	@SubBalAddtlDtls.setter
	def SubBalAddtlDtls(self, value):
		self._SubBalAddtlDtls = value if type(value) != auto else self.make_default("SubBalAddtlDtls")

	@SubBalAddtlDtls.deleter
	def SubBalAddtlDtls(self):
		del self._SubBalAddtlDtls
		self._SubBalAddtlDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlBalBrkdwnDtls', type=AdditionalBalanceInformation20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalAddtlDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Balance21, min=1, max=1, mutex_group=None, array=False),
	))

