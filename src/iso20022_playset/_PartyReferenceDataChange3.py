# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import SystemPartyIdentification8
from . import UpdateLogPartyRecord2Choice

class PartyReferenceDataChange3(base_types._BaseFieldType):

	__slots__ = ["_OprTmStmp", "_PtyId", "_Rcrd"]
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
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification8, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification8, False)

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
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=UpdateLogPartyRecord2Choice, min=1, max=None, mutex_group=None, array=True),
	))