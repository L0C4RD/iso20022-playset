# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection44

class CollateralAmount5(base_types._BaseFieldType):

	__slots__ = ["_Collsd", "_ReqrdMrgn", "_RmngCollsd", "_RmngSttlm", "_Sttld"]
	@property
	def Collsd(self):
		return self._Collsd

	@Collsd.setter
	def Collsd(self, value):
		self._Collsd = value if value is not None else base_types.UninitialisedField(self, 'Collsd', AmountAndDirection44, False)

	@Collsd.deleter
	def Collsd(self):
		del self._Collsd
		self._Collsd = base_types.UninitialisedField(self, 'Collsd', AmountAndDirection44, False)

	@property
	def ReqrdMrgn(self):
		return self._ReqrdMrgn

	@ReqrdMrgn.setter
	def ReqrdMrgn(self, value):
		self._ReqrdMrgn = value if value is not None else base_types.UninitialisedField(self, 'ReqrdMrgn', AmountAndDirection44, False)

	@ReqrdMrgn.deleter
	def ReqrdMrgn(self):
		del self._ReqrdMrgn
		self._ReqrdMrgn = base_types.UninitialisedField(self, 'ReqrdMrgn', AmountAndDirection44, False)

	@property
	def RmngCollsd(self):
		return self._RmngCollsd

	@RmngCollsd.setter
	def RmngCollsd(self, value):
		self._RmngCollsd = value if value is not None else base_types.UninitialisedField(self, 'RmngCollsd', AmountAndDirection44, False)

	@RmngCollsd.deleter
	def RmngCollsd(self):
		del self._RmngCollsd
		self._RmngCollsd = base_types.UninitialisedField(self, 'RmngCollsd', AmountAndDirection44, False)

	@property
	def RmngSttlm(self):
		return self._RmngSttlm

	@RmngSttlm.setter
	def RmngSttlm(self, value):
		self._RmngSttlm = value if value is not None else base_types.UninitialisedField(self, 'RmngSttlm', AmountAndDirection44, False)

	@RmngSttlm.deleter
	def RmngSttlm(self):
		del self._RmngSttlm
		self._RmngSttlm = base_types.UninitialisedField(self, 'RmngSttlm', AmountAndDirection44, False)

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if value is not None else base_types.UninitialisedField(self, 'Sttld', AmountAndDirection44, False)

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = base_types.UninitialisedField(self, 'Sttld', AmountAndDirection44, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Collsd', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdMrgn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngCollsd', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngSttlm', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
	))