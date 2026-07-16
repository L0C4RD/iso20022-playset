# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HoldingAccountLevel1Code
from . import ISODate
from . import SecuritiesAccount19
from . import SecurityIdentification19

class ReportItem1(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctLvl", "_FinInstrmId", "_ItmDt"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', SecuritiesAccount19, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', SecuritiesAccount19, False)

	@property
	def AcctLvl(self):
		return self._AcctLvl

	@AcctLvl.setter
	def AcctLvl(self, value):
		self._AcctLvl = value if value is not None else base_types.UninitialisedField(self, 'AcctLvl', HoldingAccountLevel1Code, False)

	@AcctLvl.deleter
	def AcctLvl(self):
		del self._AcctLvl
		self._AcctLvl = base_types.UninitialisedField(self, 'AcctLvl', HoldingAccountLevel1Code, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def ItmDt(self):
		return self._ItmDt

	@ItmDt.setter
	def ItmDt(self, value):
		self._ItmDt = value if value is not None else base_types.UninitialisedField(self, 'ItmDt', ISODate, False)

	@ItmDt.deleter
	def ItmDt(self):
		del self._ItmDt
		self._ItmDt = base_types.UninitialisedField(self, 'ItmDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctLvl', type=HoldingAccountLevel1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))