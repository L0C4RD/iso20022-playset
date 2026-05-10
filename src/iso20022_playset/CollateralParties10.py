import base_types
import PartyIdentificationAndAccount202
import PartyIdentificationAndAccount203
import SecuritiesAccount19
import PartyIdentification136

class CollateralParties10(base_types._BaseFieldType):

	__slots__ = ["_TrptyAgt", "_PtyB", "_CollAcct", "_ClntPtyA", "_ClntPtyB", "_PtyA"]
	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if type(value) != auto else self.make_default("TrptyAgt")

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = None

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if type(value) != auto else self.make_default("PtyB")

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = None

	@property
	def CollAcct(self):
		return self._CollAcct

	@CollAcct.setter
	def CollAcct(self, value):
		self._CollAcct = value if type(value) != auto else self.make_default("CollAcct")

	@CollAcct.deleter
	def CollAcct(self):
		del self._CollAcct
		self._CollAcct = None

	@property
	def ClntPtyA(self):
		return self._ClntPtyA

	@ClntPtyA.setter
	def ClntPtyA(self, value):
		self._ClntPtyA = value if type(value) != auto else self.make_default("ClntPtyA")

	@ClntPtyA.deleter
	def ClntPtyA(self):
		del self._ClntPtyA
		self._ClntPtyA = None

	@property
	def ClntPtyB(self):
		return self._ClntPtyB

	@ClntPtyB.setter
	def ClntPtyB(self, value):
		self._ClntPtyB = value if type(value) != auto else self.make_default("ClntPtyB")

	@ClntPtyB.deleter
	def ClntPtyB(self):
		del self._ClntPtyB
		self._ClntPtyB = None

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if type(value) != auto else self.make_default("PtyA")

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentificationAndAccount203, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntPtyA', type=PartyIdentificationAndAccount202, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntPtyB', type=PartyIdentificationAndAccount203, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentificationAndAccount202, min=1, max=1, mutex_group=None, array=False),
	))

