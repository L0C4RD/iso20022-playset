# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max256Text
from . import UpdateLogPartyRecord2Choice

class PartyAuditTrail2(base_types._BaseFieldType):

	__slots__ = ["_ApprvgUsr", "_InstgUsr", "_OprTmStmp", "_Rcrd"]
	@property
	def ApprvgUsr(self):
		return self._ApprvgUsr

	@ApprvgUsr.setter
	def ApprvgUsr(self, value):
		self._ApprvgUsr = value if value is not None else base_types.UninitialisedField(self, 'ApprvgUsr', Max256Text, False)

	@ApprvgUsr.deleter
	def ApprvgUsr(self):
		del self._ApprvgUsr
		self._ApprvgUsr = base_types.UninitialisedField(self, 'ApprvgUsr', Max256Text, False)

	@property
	def InstgUsr(self):
		return self._InstgUsr

	@InstgUsr.setter
	def InstgUsr(self, value):
		self._InstgUsr = value if value is not None else base_types.UninitialisedField(self, 'InstgUsr', Max256Text, False)

	@InstgUsr.deleter
	def InstgUsr(self):
		del self._InstgUsr
		self._InstgUsr = base_types.UninitialisedField(self, 'InstgUsr', Max256Text, False)

	@property
	def OprTmStmp(self):
		return self._OprTmStmp

	@OprTmStmp.setter
	def OprTmStmp(self, value):
		self._OprTmStmp = value if value is not None else base_types.UninitialisedField(self, 'OprTmStmp', ISODateTime, False)

	@OprTmStmp.deleter
	def OprTmStmp(self):
		del self._OprTmStmp
		self._OprTmStmp = base_types.UninitialisedField(self, 'OprTmStmp', ISODateTime, False)

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if value is not None else base_types.UninitialisedField(self, 'Rcrd', UpdateLogPartyRecord2Choice, True)

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = base_types.UninitialisedField(self, 'Rcrd', UpdateLogPartyRecord2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvgUsr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgUsr', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=UpdateLogPartyRecord2Choice, min=1, max=None, mutex_group=None, array=True),
	))