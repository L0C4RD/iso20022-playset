# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClassificationType32Choice
from . import GenericIdentification1
from . import Max350Text
from . import Max35Text
from . import SecurityIdentification46Choice

class FinancialInstrumentIdentification9(base_types._BaseFieldType):

	__slots__ = ["_AltrnSctyTp", "_ClssfctnTp", "_Id", "_Nm", "_ShrtNm"]
	@property
	def AltrnSctyTp(self):
		return self._AltrnSctyTp

	@AltrnSctyTp.setter
	def AltrnSctyTp(self, value):
		self._AltrnSctyTp = value if value is not None else base_types.UninitialisedField(self, 'AltrnSctyTp', GenericIdentification1, False)

	@AltrnSctyTp.deleter
	def AltrnSctyTp(self):
		del self._AltrnSctyTp
		self._AltrnSctyTp = base_types.UninitialisedField(self, 'AltrnSctyTp', GenericIdentification1, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType32Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType32Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification46Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification46Choice, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnSctyTp', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))