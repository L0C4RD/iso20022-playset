# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification139

class AdditionalReference10(base_types._BaseFieldType):

	__slots__ = ["_MsgNm", "_Ref", "_RefIssr"]
	@property
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if value is not None else base_types.UninitialisedField(self, 'MsgNm', Max35Text, False)

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = base_types.UninitialisedField(self, 'MsgNm', Max35Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def RefIssr(self):
		return self._RefIssr

	@RefIssr.setter
	def RefIssr(self, value):
		self._RefIssr = value if value is not None else base_types.UninitialisedField(self, 'RefIssr', PartyIdentification139, False)

	@RefIssr.deleter
	def RefIssr(self):
		del self._RefIssr
		self._RefIssr = base_types.UninitialisedField(self, 'RefIssr', PartyIdentification139, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefIssr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
	))