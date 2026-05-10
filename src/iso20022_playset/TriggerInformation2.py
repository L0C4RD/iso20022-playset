import base_types
import Max70Text
import ExchangePolicy2Code
import PartyType5Code
import Max35Text

class TriggerInformation2(base_types._BaseFieldType):

	__slots__ = ["_TrggrTp", "_AddtlInf", "_TrggrSrc", "_SrcId"]
	@property
	def TrggrTp(self):
		return self._TrggrTp

	@TrggrTp.setter
	def TrggrTp(self, value):
		self._TrggrTp = value if type(value) != auto else self.make_default("TrggrTp")

	@TrggrTp.deleter
	def TrggrTp(self):
		del self._TrggrTp
		self._TrggrTp = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def TrggrSrc(self):
		return self._TrggrSrc

	@TrggrSrc.setter
	def TrggrSrc(self, value):
		self._TrggrSrc = value if type(value) != auto else self.make_default("TrggrSrc")

	@TrggrSrc.deleter
	def TrggrSrc(self):
		del self._TrggrSrc
		self._TrggrSrc = None

	@property
	def SrcId(self):
		return self._SrcId

	@SrcId.setter
	def SrcId(self, value):
		self._SrcId = value if type(value) != auto else self.make_default("SrcId")

	@SrcId.deleter
	def SrcId(self):
		del self._SrcId
		self._SrcId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrggrTp', type=ExchangePolicy2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrggrSrc', type=PartyType5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

