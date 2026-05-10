import base_types
import EventDescription1
import Max15NumericText
import BusinessLetter1
import EncapsulatedBusinessMessage1

class PartyEventAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AttchdMsg", "_EvtCnt", "_Hdr", "_EvtNtce"]
	@property
	def AttchdMsg(self):
		return self._AttchdMsg

	@AttchdMsg.setter
	def AttchdMsg(self, value):
		self._AttchdMsg = value if type(value) != auto else self.make_default("AttchdMsg")

	@AttchdMsg.deleter
	def AttchdMsg(self):
		del self._AttchdMsg
		self._AttchdMsg = None

	@property
	def EvtCnt(self):
		return self._EvtCnt

	@EvtCnt.setter
	def EvtCnt(self, value):
		self._EvtCnt = value if type(value) != auto else self.make_default("EvtCnt")

	@EvtCnt.deleter
	def EvtCnt(self):
		del self._EvtCnt
		self._EvtCnt = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def EvtNtce(self):
		return self._EvtNtce

	@EvtNtce.setter
	def EvtNtce(self, value):
		self._EvtNtce = value if type(value) != auto else self.make_default("EvtNtce")

	@EvtNtce.deleter
	def EvtNtce(self):
		del self._EvtNtce
		self._EvtNtce = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdMsg', type=EncapsulatedBusinessMessage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtCnt', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=BusinessLetter1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtNtce', type=EventDescription1, min=1, max=None, mutex_group=None, array=True),
	))

