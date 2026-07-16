# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessLetter1
from . import EncapsulatedBusinessMessage1
from . import EventDescription1
from . import Max15NumericText

class PartyEventAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AttchdMsg", "_EvtCnt", "_EvtNtce", "_Hdr"]
	@property
	def AttchdMsg(self):
		return self._AttchdMsg

	@AttchdMsg.setter
	def AttchdMsg(self, value):
		self._AttchdMsg = value if value is not None else base_types.UninitialisedField(self, 'AttchdMsg', EncapsulatedBusinessMessage1, True)

	@AttchdMsg.deleter
	def AttchdMsg(self):
		del self._AttchdMsg
		self._AttchdMsg = base_types.UninitialisedField(self, 'AttchdMsg', EncapsulatedBusinessMessage1, True)

	@property
	def EvtCnt(self):
		return self._EvtCnt

	@EvtCnt.setter
	def EvtCnt(self, value):
		self._EvtCnt = value if value is not None else base_types.UninitialisedField(self, 'EvtCnt', Max15NumericText, False)

	@EvtCnt.deleter
	def EvtCnt(self):
		del self._EvtCnt
		self._EvtCnt = base_types.UninitialisedField(self, 'EvtCnt', Max15NumericText, False)

	@property
	def EvtNtce(self):
		return self._EvtNtce

	@EvtNtce.setter
	def EvtNtce(self, value):
		self._EvtNtce = value if value is not None else base_types.UninitialisedField(self, 'EvtNtce', EventDescription1, True)

	@EvtNtce.deleter
	def EvtNtce(self):
		del self._EvtNtce
		self._EvtNtce = base_types.UninitialisedField(self, 'EvtNtce', EventDescription1, True)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', BusinessLetter1, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', BusinessLetter1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtNtce', type=EventDescription1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
	))