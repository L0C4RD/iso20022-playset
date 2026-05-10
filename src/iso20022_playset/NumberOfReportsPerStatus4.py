import base_types
import PairedReconciled3Code
import Max15NumericText

class NumberOfReportsPerStatus4(base_types._BaseFieldType):

	__slots__ = ["_DtldSts", "_DtldNbOfRpts"]
	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if type(value) != auto else self.make_default("DtldSts")

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = None

	@property
	def DtldNbOfRpts(self):
		return self._DtldNbOfRpts

	@DtldNbOfRpts.setter
	def DtldNbOfRpts(self, value):
		self._DtldNbOfRpts = value if type(value) != auto else self.make_default("DtldNbOfRpts")

	@DtldNbOfRpts.deleter
	def DtldNbOfRpts(self):
		del self._DtldNbOfRpts
		self._DtldNbOfRpts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldSts', type=PairedReconciled3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldNbOfRpts', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

