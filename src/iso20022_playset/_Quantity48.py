from . import base_types
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._Max210Text import Max210Text
from ._QuantityBreakdown62 import QuantityBreakdown62
from ._SecuritiesCertificate4 import SecuritiesCertificate4

class Quantity48(base_types._BaseFieldType):

	__slots__ = ["_CertNb", "_DnmtnChc", "_QtyBrkdwn", "_SttlmQty"]
	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if type(value) != base_types.auto else self.make_default("CertNb")

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = None

	@property
	def DnmtnChc(self):
		return self._DnmtnChc

	@DnmtnChc.setter
	def DnmtnChc(self, value):
		self._DnmtnChc = value if type(value) != base_types.auto else self.make_default("DnmtnChc")

	@DnmtnChc.deleter
	def DnmtnChc(self):
		del self._DnmtnChc
		self._DnmtnChc = None

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != base_types.auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != base_types.auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertNb', type=SecuritiesCertificate4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DnmtnChc', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown62, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
	))

