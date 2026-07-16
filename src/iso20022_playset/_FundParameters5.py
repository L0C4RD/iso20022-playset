# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import FinancialInstrument71
from . import ISODate
from . import PartyIdentification139

class FundParameters5(base_types._BaseFieldType):

	__slots__ = ["_CtryOfDmcl", "_DtFr", "_FinInstrmDtls", "_FndMgmtCpny", "_RegdDstrbtnCtry"]
	@property
	def CtryOfDmcl(self):
		return self._CtryOfDmcl

	@CtryOfDmcl.setter
	def CtryOfDmcl(self, value):
		self._CtryOfDmcl = value if value is not None else base_types.UninitialisedField(self, 'CtryOfDmcl', CountryCode, False)

	@CtryOfDmcl.deleter
	def CtryOfDmcl(self):
		del self._CtryOfDmcl
		self._CtryOfDmcl = base_types.UninitialisedField(self, 'CtryOfDmcl', CountryCode, False)

	@property
	def DtFr(self):
		return self._DtFr

	@DtFr.setter
	def DtFr(self, value):
		self._DtFr = value if value is not None else base_types.UninitialisedField(self, 'DtFr', ISODate, False)

	@DtFr.deleter
	def DtFr(self):
		del self._DtFr
		self._DtFr = base_types.UninitialisedField(self, 'DtFr', ISODate, False)

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument71, True)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument71, True)

	@property
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if value is not None else base_types.UninitialisedField(self, 'FndMgmtCpny', PartyIdentification139, True)

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = base_types.UninitialisedField(self, 'FndMgmtCpny', PartyIdentification139, True)

	@property
	def RegdDstrbtnCtry(self):
		return self._RegdDstrbtnCtry

	@RegdDstrbtnCtry.setter
	def RegdDstrbtnCtry(self, value):
		self._RegdDstrbtnCtry = value if value is not None else base_types.UninitialisedField(self, 'RegdDstrbtnCtry', CountryCode, True)

	@RegdDstrbtnCtry.deleter
	def RegdDstrbtnCtry(self):
		del self._RegdDstrbtnCtry
		self._RegdDstrbtnCtry = base_types.UninitialisedField(self, 'RegdDstrbtnCtry', CountryCode, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryOfDmcl', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument71, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndMgmtCpny', type=PartyIdentification139, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdDstrbtnCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
	))