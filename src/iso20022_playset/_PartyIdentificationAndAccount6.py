# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount7
from . import PartyIdentification25

class PartyIdentificationAndAccount6(base_types._BaseFieldType):

	__slots__ = ["_CdtAcct", "_FincgAcct", "_PtyId"]
	@property
	def CdtAcct(self):
		return self._CdtAcct

	@CdtAcct.setter
	def CdtAcct(self, value):
		self._CdtAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtAcct', CashAccount7, False)

	@CdtAcct.deleter
	def CdtAcct(self):
		del self._CdtAcct
		self._CdtAcct = base_types.UninitialisedField(self, 'CdtAcct', CashAccount7, False)

	@property
	def FincgAcct(self):
		return self._FincgAcct

	@FincgAcct.setter
	def FincgAcct(self, value):
		self._FincgAcct = value if value is not None else base_types.UninitialisedField(self, 'FincgAcct', CashAccount7, False)

	@FincgAcct.deleter
	def FincgAcct(self):
		del self._FincgAcct
		self._FincgAcct = base_types.UninitialisedField(self, 'FincgAcct', CashAccount7, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification25, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification25, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification25, min=1, max=1, mutex_group=None, array=False),
	))