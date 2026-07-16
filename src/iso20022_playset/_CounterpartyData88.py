# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyData89
from . import ISODateTime
from . import OrganisationIdentification15Choice

class CounterpartyData88(base_types._BaseFieldType):

	__slots__ = ["_CtrPty", "_RptSubmitgNtty", "_RptgDtTm"]
	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', CounterpartyData89, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', CounterpartyData89, False)

	@property
	def RptSubmitgNtty(self):
		return self._RptSubmitgNtty

	@RptSubmitgNtty.setter
	def RptSubmitgNtty(self, value):
		self._RptSubmitgNtty = value if value is not None else base_types.UninitialisedField(self, 'RptSubmitgNtty', OrganisationIdentification15Choice, False)

	@RptSubmitgNtty.deleter
	def RptSubmitgNtty(self):
		del self._RptSubmitgNtty
		self._RptSubmitgNtty = base_types.UninitialisedField(self, 'RptSubmitgNtty', OrganisationIdentification15Choice, False)

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptgDtTm', ISODateTime, False)

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = base_types.UninitialisedField(self, 'RptgDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPty', type=CounterpartyData89, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSubmitgNtty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))