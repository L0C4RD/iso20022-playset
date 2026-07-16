# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber5Choice
from . import PartyIdentification127Choice
from . import ProcessingPosition8Choice
from . import References80Choice

class Linkages73(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_PrcgPos", "_Ref", "_RefOwnr"]
	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if value is not None else base_types.UninitialisedField(self, 'MsgNb', DocumentNumber5Choice, False)

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = base_types.UninitialisedField(self, 'MsgNb', DocumentNumber5Choice, False)

	@property
	def PrcgPos(self):
		return self._PrcgPos

	@PrcgPos.setter
	def PrcgPos(self, value):
		self._PrcgPos = value if value is not None else base_types.UninitialisedField(self, 'PrcgPos', ProcessingPosition8Choice, False)

	@PrcgPos.deleter
	def PrcgPos(self):
		del self._PrcgPos
		self._PrcgPos = base_types.UninitialisedField(self, 'PrcgPos', ProcessingPosition8Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References80Choice, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References80Choice, False)

	@property
	def RefOwnr(self):
		return self._RefOwnr

	@RefOwnr.setter
	def RefOwnr(self, value):
		self._RefOwnr = value if value is not None else base_types.UninitialisedField(self, 'RefOwnr', PartyIdentification127Choice, False)

	@RefOwnr.deleter
	def RefOwnr(self):
		del self._RefOwnr
		self._RefOwnr = base_types.UninitialisedField(self, 'RefOwnr', PartyIdentification127Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References80Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefOwnr', type=PartyIdentification127Choice, min=0, max=1, mutex_group=None, array=False),
	))