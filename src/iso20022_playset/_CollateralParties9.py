# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification136
from . import PartyIdentificationAndAccount202

class CollateralParties9(base_types._BaseFieldType):

	__slots__ = ["_ClntPtyA", "_PtyA", "_TrptyAgt"]
	@property
	def ClntPtyA(self):
		return self._ClntPtyA

	@ClntPtyA.setter
	def ClntPtyA(self, value):
		self._ClntPtyA = value if value is not None else base_types.UninitialisedField(self, 'ClntPtyA', PartyIdentificationAndAccount202, False)

	@ClntPtyA.deleter
	def ClntPtyA(self):
		del self._ClntPtyA
		self._ClntPtyA = base_types.UninitialisedField(self, 'ClntPtyA', PartyIdentificationAndAccount202, False)

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if value is not None else base_types.UninitialisedField(self, 'PtyA', PartyIdentificationAndAccount202, False)

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = base_types.UninitialisedField(self, 'PtyA', PartyIdentificationAndAccount202, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentification136, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntPtyA', type=PartyIdentificationAndAccount202, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentificationAndAccount202, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))