# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CategoryPurpose1Choice import CategoryPurpose1Choice
from ._LocalInstrument2Choice import LocalInstrument2Choice
from ._MandateClassification1Choice import MandateClassification1Choice
from ._ServiceLevel8Choice import ServiceLevel8Choice

class MandateTypeInformation2(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_CtgyPurp", "_LclInstrm", "_SvcLvl"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if type(value) != base_types.auto else self.make_default("Clssfctn")

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = None

	@property
	def CtgyPurp(self):
		return self._CtgyPurp

	@CtgyPurp.setter
	def CtgyPurp(self, value):
		self._CtgyPurp = value if type(value) != base_types.auto else self.make_default("CtgyPurp")

	@CtgyPurp.deleter
	def CtgyPurp(self):
		del self._CtgyPurp
		self._CtgyPurp = None

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if type(value) != base_types.auto else self.make_default("LclInstrm")

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = None

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if type(value) != base_types.auto else self.make_default("SvcLvl")

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=MandateClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtgyPurp', type=CategoryPurpose1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=LocalInstrument2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvl', type=ServiceLevel8Choice, min=0, max=1, mutex_group=None, array=False),
	))