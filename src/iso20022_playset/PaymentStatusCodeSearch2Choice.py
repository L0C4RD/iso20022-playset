import base_types
import CashPaymentStatus2Code
import PendingStatus4Code
import FinalStatusCode

class PaymentStatusCodeSearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgAndFnlSts", "_PdgSts", "_FnlSts"]
	@property
	def PdgAndFnlSts(self):
		return self._PdgAndFnlSts

	@PdgAndFnlSts.setter
	def PdgAndFnlSts(self, value):
		self._PdgAndFnlSts = value if type(value) != auto else self.make_default("PdgAndFnlSts")

	@PdgAndFnlSts.deleter
	def PdgAndFnlSts(self):
		del self._PdgAndFnlSts
		self._PdgAndFnlSts = None

	@property
	def PdgSts(self):
		return self._PdgSts

	@PdgSts.setter
	def PdgSts(self, value):
		self._PdgSts = value if type(value) != auto else self.make_default("PdgSts")

	@PdgSts.deleter
	def PdgSts(self):
		del self._PdgSts
		self._PdgSts = None

	@property
	def FnlSts(self):
		return self._FnlSts

	@FnlSts.setter
	def FnlSts(self, value):
		self._FnlSts = value if type(value) != auto else self.make_default("FnlSts")

	@FnlSts.deleter
	def FnlSts(self):
		del self._FnlSts
		self._FnlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgAndFnlSts', type=CashPaymentStatus2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSts', type=PendingStatus4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FnlSts', type=FinalStatusCode, min=0, max=1, mutex_group=1, array=False),
	))

