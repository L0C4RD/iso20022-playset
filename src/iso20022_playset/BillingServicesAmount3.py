from . import base_types
import AmountAndDirection34

class BillingServicesAmount3(base_types._BaseFieldType):

	__slots__ = ["_SrcAmt", "_HstAmt"]
	@property
	def SrcAmt(self):
		return self._SrcAmt

	@SrcAmt.setter
	def SrcAmt(self, value):
		self._SrcAmt = value if type(value) != auto else self.make_default("SrcAmt")

	@SrcAmt.deleter
	def SrcAmt(self):
		del self._SrcAmt
		self._SrcAmt = None

	@property
	def HstAmt(self):
		return self._HstAmt

	@HstAmt.setter
	def HstAmt(self, value):
		self._HstAmt = value if type(value) != auto else self.make_default("HstAmt")

	@HstAmt.deleter
	def HstAmt(self):
		del self._HstAmt
		self._HstAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrcAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

