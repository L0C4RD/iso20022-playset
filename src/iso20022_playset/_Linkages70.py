# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentNumber6Choice import DocumentNumber6Choice
from ._PairedOrTurnedQuantity6Choice import PairedOrTurnedQuantity6Choice
from ._ProcessingPosition10Choice import ProcessingPosition10Choice
from ._References58Choice import References58Choice

class Linkages70(base_types._BaseFieldType):

	__slots__ = ["_LkdQty", "_MsgNb", "_PrcgPos", "_Ref"]
	@property
	def LkdQty(self):
		return self._LkdQty

	@LkdQty.setter
	def LkdQty(self, value):
		self._LkdQty = value if type(value) != base_types.auto else self.make_default("LkdQty")

	@LkdQty.deleter
	def LkdQty(self):
		del self._LkdQty
		self._LkdQty = None

	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if type(value) != base_types.auto else self.make_default("MsgNb")

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = None

	@property
	def PrcgPos(self):
		return self._PrcgPos

	@PrcgPos.setter
	def PrcgPos(self, value):
		self._PrcgPos = value if type(value) != base_types.auto else self.make_default("PrcgPos")

	@PrcgPos.deleter
	def PrcgPos(self):
		del self._PrcgPos
		self._PrcgPos = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdQty', type=PairedOrTurnedQuantity6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References58Choice, min=1, max=1, mutex_group=None, array=False),
	))