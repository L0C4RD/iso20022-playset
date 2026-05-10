import base_types
import TradeTransactionIdentification24
import GenericValidationRuleIdentification1
import ReportingMessageStatus2Code

class RejectionReason71(base_types._BaseFieldType):

	__slots__ = ["_DtldVldtnRule", "_Sts", "_TxId"]
	@property
	def DtldVldtnRule(self):
		return self._DtldVldtnRule

	@DtldVldtnRule.setter
	def DtldVldtnRule(self, value):
		self._DtldVldtnRule = value if type(value) != auto else self.make_default("DtldVldtnRule")

	@DtldVldtnRule.deleter
	def DtldVldtnRule(self):
		del self._DtldVldtnRule
		self._DtldVldtnRule = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldVldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ReportingMessageStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
	))

