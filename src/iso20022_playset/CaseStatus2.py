import base_types
import ISODateTime
import Max140Text
import CaseStatus2Code

class CaseStatus2(base_types._BaseFieldType):

	__slots__ = ["_CaseSts", "_Rsn", "_DtTm"]
	@property
	def CaseSts(self):
		return self._CaseSts

	@CaseSts.setter
	def CaseSts(self, value):
		self._CaseSts = value if type(value) != auto else self.make_default("CaseSts")

	@CaseSts.deleter
	def CaseSts(self):
		del self._CaseSts
		self._CaseSts = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CaseSts', type=CaseStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

