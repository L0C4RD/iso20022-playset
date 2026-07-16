# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity33Choice
from . import Max210Text
from . import QuantityBreakdown62
from . import SecuritiesCertificate4

class Quantity48(base_types._BaseFieldType):

	__slots__ = ["_CertNb", "_DnmtnChc", "_QtyBrkdwn", "_SttlmQty"]
	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', SecuritiesCertificate4, True)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', SecuritiesCertificate4, True)

	@property
	def DnmtnChc(self):
		return self._DnmtnChc

	@DnmtnChc.setter
	def DnmtnChc(self, value):
		self._DnmtnChc = value if value is not None else base_types.UninitialisedField(self, 'DnmtnChc', Max210Text, False)

	@DnmtnChc.deleter
	def DnmtnChc(self):
		del self._DnmtnChc
		self._DnmtnChc = base_types.UninitialisedField(self, 'DnmtnChc', Max210Text, False)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown62, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown62, True)

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if value is not None else base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity33Choice, False)

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity33Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertNb', type=SecuritiesCertificate4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DnmtnChc', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown62, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
	))