# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import Number
from . import TaxOrganisationIdentification1

class TaxReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_NbOfTaxRpts", "_TaxAuthrty"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def NbOfTaxRpts(self):
		return self._NbOfTaxRpts

	@NbOfTaxRpts.setter
	def NbOfTaxRpts(self, value):
		self._NbOfTaxRpts = value if value is not None else base_types.UninitialisedField(self, 'NbOfTaxRpts', Number, False)

	@NbOfTaxRpts.deleter
	def NbOfTaxRpts(self):
		del self._NbOfTaxRpts
		self._NbOfTaxRpts = base_types.UninitialisedField(self, 'NbOfTaxRpts', Number, False)

	@property
	def TaxAuthrty(self):
		return self._TaxAuthrty

	@TaxAuthrty.setter
	def TaxAuthrty(self, value):
		self._TaxAuthrty = value if value is not None else base_types.UninitialisedField(self, 'TaxAuthrty', TaxOrganisationIdentification1, True)

	@TaxAuthrty.deleter
	def TaxAuthrty(self):
		del self._TaxAuthrty
		self._TaxAuthrty = base_types.UninitialisedField(self, 'TaxAuthrty', TaxOrganisationIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTaxRpts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAuthrty', type=TaxOrganisationIdentification1, min=0, max=None, mutex_group=None, array=True),
	))