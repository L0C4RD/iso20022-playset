import base_types
import TrueFalseIndicator
import Max35Text

class DiagnosisRequest1(base_types._BaseFieldType):

	__slots__ = ["_HstDgnssFlg", "_AcqrrId"]
	@property
	def HstDgnssFlg(self):
		return self._HstDgnssFlg

	@HstDgnssFlg.setter
	def HstDgnssFlg(self, value):
		self._HstDgnssFlg = value if type(value) != auto else self.make_default("HstDgnssFlg")

	@HstDgnssFlg.deleter
	def HstDgnssFlg(self):
		del self._HstDgnssFlg
		self._HstDgnssFlg = None

	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if type(value) != auto else self.make_default("AcqrrId")

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstDgnssFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

