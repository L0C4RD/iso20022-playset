from . import base_types
from ._MessageIdentification1 import MessageIdentification1
from ._Number import Number
from ._TaxOrganisationIdentification1 import TaxOrganisationIdentification1

class TaxReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_NbOfTaxRpts", "_TaxAuthrty"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def NbOfTaxRpts(self):
		return self._NbOfTaxRpts

	@NbOfTaxRpts.setter
	def NbOfTaxRpts(self, value):
		self._NbOfTaxRpts = value if type(value) != base_types.auto else self.make_default("NbOfTaxRpts")

	@NbOfTaxRpts.deleter
	def NbOfTaxRpts(self):
		del self._NbOfTaxRpts
		self._NbOfTaxRpts = None

	@property
	def TaxAuthrty(self):
		return self._TaxAuthrty

	@TaxAuthrty.setter
	def TaxAuthrty(self, value):
		self._TaxAuthrty = value if type(value) != base_types.auto else self.make_default("TaxAuthrty")

	@TaxAuthrty.deleter
	def TaxAuthrty(self):
		del self._TaxAuthrty
		self._TaxAuthrty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTaxRpts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAuthrty', type=TaxOrganisationIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

