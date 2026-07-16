# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCalculation1
from . import MarginCalculation2
from . import MarginProductType1Choice
from . import PartyIdentificationAndAccount31
from . import SecuritiesAccount18
from . import YesNoIndicator

class MarginReport2(base_types._BaseFieldType):

	__slots__ = ["_CollsdMrgnAcctInd", "_MrgnAcct", "_MrgnClctn", "_MrgnClctnSummry", "_MrgnPdct", "_NonClrMmb"]
	@property
	def CollsdMrgnAcctInd(self):
		return self._CollsdMrgnAcctInd

	@CollsdMrgnAcctInd.setter
	def CollsdMrgnAcctInd(self, value):
		self._CollsdMrgnAcctInd = value if value is not None else base_types.UninitialisedField(self, 'CollsdMrgnAcctInd', YesNoIndicator, False)

	@CollsdMrgnAcctInd.deleter
	def CollsdMrgnAcctInd(self):
		del self._CollsdMrgnAcctInd
		self._CollsdMrgnAcctInd = base_types.UninitialisedField(self, 'CollsdMrgnAcctInd', YesNoIndicator, False)

	@property
	def MrgnAcct(self):
		return self._MrgnAcct

	@MrgnAcct.setter
	def MrgnAcct(self, value):
		self._MrgnAcct = value if value is not None else base_types.UninitialisedField(self, 'MrgnAcct', SecuritiesAccount18, False)

	@MrgnAcct.deleter
	def MrgnAcct(self):
		del self._MrgnAcct
		self._MrgnAcct = base_types.UninitialisedField(self, 'MrgnAcct', SecuritiesAccount18, False)

	@property
	def MrgnClctn(self):
		return self._MrgnClctn

	@MrgnClctn.setter
	def MrgnClctn(self, value):
		self._MrgnClctn = value if value is not None else base_types.UninitialisedField(self, 'MrgnClctn', MarginCalculation2, True)

	@MrgnClctn.deleter
	def MrgnClctn(self):
		del self._MrgnClctn
		self._MrgnClctn = base_types.UninitialisedField(self, 'MrgnClctn', MarginCalculation2, True)

	@property
	def MrgnClctnSummry(self):
		return self._MrgnClctnSummry

	@MrgnClctnSummry.setter
	def MrgnClctnSummry(self, value):
		self._MrgnClctnSummry = value if value is not None else base_types.UninitialisedField(self, 'MrgnClctnSummry', MarginCalculation1, False)

	@MrgnClctnSummry.deleter
	def MrgnClctnSummry(self):
		del self._MrgnClctnSummry
		self._MrgnClctnSummry = base_types.UninitialisedField(self, 'MrgnClctnSummry', MarginCalculation1, False)

	@property
	def MrgnPdct(self):
		return self._MrgnPdct

	@MrgnPdct.setter
	def MrgnPdct(self, value):
		self._MrgnPdct = value if value is not None else base_types.UninitialisedField(self, 'MrgnPdct', MarginProductType1Choice, True)

	@MrgnPdct.deleter
	def MrgnPdct(self):
		del self._MrgnPdct
		self._MrgnPdct = base_types.UninitialisedField(self, 'MrgnPdct', MarginProductType1Choice, True)

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount31, True)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount31, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollsdMrgnAcctInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcct', type=SecuritiesAccount18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnClctn', type=MarginCalculation2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnClctnSummry', type=MarginCalculation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnPdct', type=MarginProductType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount31, min=0, max=None, mutex_group=None, array=True),
	))