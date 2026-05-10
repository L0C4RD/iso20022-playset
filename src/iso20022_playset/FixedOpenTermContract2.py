import base_types
import ISODate
import RepoTerminationOption2Code

class FixedOpenTermContract2(base_types._BaseFieldType):

	__slots__ = ["_MtrtyDt", "_TermntnOptn"]
	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if type(value) != auto else self.make_default("TermntnOptn")

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption2Code, min=0, max=1, mutex_group=None, array=False),
	))

