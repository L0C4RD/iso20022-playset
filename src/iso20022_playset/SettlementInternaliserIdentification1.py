import base_types
import ContactDetails4
import Exact2UpperCaseAlphaText
import CountryCode
import LEIIdentifier

class SettlementInternaliserIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_RspnsblPrsn", "_BrnchId", "_LEI"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def RspnsblPrsn(self):
		return self._RspnsblPrsn

	@RspnsblPrsn.setter
	def RspnsblPrsn(self, value):
		self._RspnsblPrsn = value if type(value) != auto else self.make_default("RspnsblPrsn")

	@RspnsblPrsn.deleter
	def RspnsblPrsn(self):
		del self._RspnsblPrsn
		self._RspnsblPrsn = None

	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if type(value) != auto else self.make_default("BrnchId")

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPrsn', type=ContactDetails4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrnchId', type=Exact2UpperCaseAlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

