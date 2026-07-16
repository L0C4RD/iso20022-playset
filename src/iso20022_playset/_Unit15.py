# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text
from . import UKTaxGroupUnit1Code
from . import Unit1Choice

class Unit15(base_types._BaseFieldType):

	__slots__ = ["_AcqstnDt", "_CertNb", "_Grp1Or2Units", "_OrdrDt", "_Ref", "_Units"]
	@property
	def AcqstnDt(self):
		return self._AcqstnDt

	@AcqstnDt.setter
	def AcqstnDt(self, value):
		self._AcqstnDt = value if value is not None else base_types.UninitialisedField(self, 'AcqstnDt', ISODate, False)

	@AcqstnDt.deleter
	def AcqstnDt(self):
		del self._AcqstnDt
		self._AcqstnDt = base_types.UninitialisedField(self, 'AcqstnDt', ISODate, False)

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', Max35Text, True)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', Max35Text, True)

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if value is not None else base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@property
	def OrdrDt(self):
		return self._OrdrDt

	@OrdrDt.setter
	def OrdrDt(self, value):
		self._OrdrDt = value if value is not None else base_types.UninitialisedField(self, 'OrdrDt', ISODate, False)

	@OrdrDt.deleter
	def OrdrDt(self):
		del self._OrdrDt
		self._OrdrDt = base_types.UninitialisedField(self, 'OrdrDt', ISODate, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def Units(self):
		return self._Units

	@Units.setter
	def Units(self, value):
		self._Units = value if value is not None else base_types.UninitialisedField(self, 'Units', Unit1Choice, False)

	@Units.deleter
	def Units(self):
		del self._Units
		self._Units = base_types.UninitialisedField(self, 'Units', Unit1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqstnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Units', type=Unit1Choice, min=1, max=1, mutex_group=None, array=False),
	))