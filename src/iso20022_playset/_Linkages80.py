# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber5Choice
from . import PairedOrTurnedQuantity7Choice
from . import ProcessingPosition7Choice
from . import References47Choice

class Linkages80(base_types._BaseFieldType):

	__slots__ = ["_LkdQty", "_MsgNb", "_PrcgPos", "_Ref"]
	@property
	def LkdQty(self):
		return self._LkdQty

	@LkdQty.setter
	def LkdQty(self, value):
		self._LkdQty = value if value is not None else base_types.UninitialisedField(self, 'LkdQty', PairedOrTurnedQuantity7Choice, False)

	@LkdQty.deleter
	def LkdQty(self):
		del self._LkdQty
		self._LkdQty = base_types.UninitialisedField(self, 'LkdQty', PairedOrTurnedQuantity7Choice, False)

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
		self._PrcgPos = value if value is not None else base_types.UninitialisedField(self, 'PrcgPos', ProcessingPosition7Choice, False)

	@PrcgPos.deleter
	def PrcgPos(self):
		del self._PrcgPos
		self._PrcgPos = base_types.UninitialisedField(self, 'PrcgPos', ProcessingPosition7Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References47Choice, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References47Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdQty', type=PairedOrTurnedQuantity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References47Choice, min=1, max=1, mutex_group=None, array=False),
	))