import base_types
import SecuritiesAccount18
import MarginCalculation2
import YesNoIndicator
import MarginProductType1Choice
import PartyIdentificationAndAccount31
import MarginCalculation1

class MarginReport2(base_types._BaseFieldType):

	__slots__ = ["_CollsdMrgnAcctInd", "_MrgnPdct", "_NonClrMmb", "_MrgnClctn", "_MrgnClctnSummry", "_MrgnAcct"]
	@property
	def CollsdMrgnAcctInd(self):
		return self._CollsdMrgnAcctInd

	@CollsdMrgnAcctInd.setter
	def CollsdMrgnAcctInd(self, value):
		self._CollsdMrgnAcctInd = value if type(value) != auto else self.make_default("CollsdMrgnAcctInd")

	@CollsdMrgnAcctInd.deleter
	def CollsdMrgnAcctInd(self):
		del self._CollsdMrgnAcctInd
		self._CollsdMrgnAcctInd = None

	@property
	def MrgnPdct(self):
		return self._MrgnPdct

	@MrgnPdct.setter
	def MrgnPdct(self, value):
		self._MrgnPdct = value if type(value) != auto else self.make_default("MrgnPdct")

	@MrgnPdct.deleter
	def MrgnPdct(self):
		del self._MrgnPdct
		self._MrgnPdct = None

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	@property
	def MrgnClctn(self):
		return self._MrgnClctn

	@MrgnClctn.setter
	def MrgnClctn(self, value):
		self._MrgnClctn = value if type(value) != auto else self.make_default("MrgnClctn")

	@MrgnClctn.deleter
	def MrgnClctn(self):
		del self._MrgnClctn
		self._MrgnClctn = None

	@property
	def MrgnClctnSummry(self):
		return self._MrgnClctnSummry

	@MrgnClctnSummry.setter
	def MrgnClctnSummry(self, value):
		self._MrgnClctnSummry = value if type(value) != auto else self.make_default("MrgnClctnSummry")

	@MrgnClctnSummry.deleter
	def MrgnClctnSummry(self):
		del self._MrgnClctnSummry
		self._MrgnClctnSummry = None

	@property
	def MrgnAcct(self):
		return self._MrgnAcct

	@MrgnAcct.setter
	def MrgnAcct(self, value):
		self._MrgnAcct = value if type(value) != auto else self.make_default("MrgnAcct")

	@MrgnAcct.deleter
	def MrgnAcct(self):
		del self._MrgnAcct
		self._MrgnAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollsdMrgnAcctInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnPdct', type=MarginProductType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount31, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnClctn', type=MarginCalculation2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnClctnSummry', type=MarginCalculation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcct', type=SecuritiesAccount18, min=1, max=1, mutex_group=None, array=False),
	))

