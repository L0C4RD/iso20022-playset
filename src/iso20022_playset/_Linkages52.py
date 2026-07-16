# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber17Choice
from . import IdentificationReference8Choice

class Linkages52(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_Ref"]
	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if value is not None else base_types.UninitialisedField(self, 'MsgNb', DocumentNumber17Choice, False)

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = base_types.UninitialisedField(self, 'MsgNb', DocumentNumber17Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', IdentificationReference8Choice, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', IdentificationReference8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=IdentificationReference8Choice, min=1, max=1, mutex_group=None, array=False),
	))