import base_types
import GenericIdentification86
import CFIOct2015Identifier

class ClassificationType33Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrnClssfctn", "_ClssfctnFinInstrm"]
	@property
	def AltrnClssfctn(self):
		return self._AltrnClssfctn

	@AltrnClssfctn.setter
	def AltrnClssfctn(self, value):
		self._AltrnClssfctn = value if type(value) != auto else self.make_default("AltrnClssfctn")

	@AltrnClssfctn.deleter
	def AltrnClssfctn(self):
		del self._AltrnClssfctn
		self._AltrnClssfctn = None

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if type(value) != auto else self.make_default("ClssfctnFinInstrm")

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnClssfctn', type=GenericIdentification86, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
	))

